import motor.motor_asyncio
from config import Config
from .utils import send_log
from datetime import datetime, timedelta

class Database:
    def __init__(self, uri, database_name):
        self._client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        self.db = self._client[database_name]
        self.col = self.db.user

    def new_user(self, id):
        return dict(
            _id=int(id),
            is_prime=False,
            prime_expiry=None,
            auth_users=[]
        )

    async def add_user(self, user_id):
        if not await self.is_user_exist(user_id):
            user = self.new_user(user_id)
            await self.col.insert_one(user)

    async def is_user_exist(self, id):
        user = await self.col.find_one({'_id': int(id)})
        return bool(user)

    async def promote_to_prime(self, user_id, duration: str):
        expiry_date = self.calculate_expiry_date(duration)
        result = await self.col.update_one(
            {'_id': int(user_id)},
            {'$set': {'is_prime': True, 'prime_expiry': expiry_date}}
        )
        return result.modified_count

    async def delete_prime_user(self, user_id):
        result = await self.col.update_one(
            {'_id': int(user_id)},
            {'$set': {'is_prime': False, 'prime_expiry': None}}
        )
        return result.modified_count

    async def is_prime_user(self, user_id):
        user = await self.col.find_one({'_id': int(user_id)})
        if user:
            is_prime = user.get('is_prime', False)
            prime_expiry = user.get('prime_expiry', None)
            if is_prime and prime_expiry and datetime.utcnow() > prime_expiry:
                # Prime status expired, update the user
                await self.delete_prime_user(user_id)
                is_prime = False
            return is_prime
        return False

    def calculate_expiry_date(self, duration: str):
        now = datetime.utcnow()
        if duration.endswith('m'):
            return now + timedelta(minutes=int(duration[:-1]))
        elif duration.endswith('h'):
            return now + timedelta(hours=int(duration[:-1]))
        elif duration.endswith('d'):
            return now + timedelta(days=int(duration[:-1]))
        elif duration.endswith('y'):
            return now + timedelta(days=365 * int(duration[:-1]))
        else:
            raise ValueError('Invalid duration format. Use 1m, 1h, 1d, or 1y.')

    async def get_prime_users(self):
        users = self.col.find({'is_prime': True})
        return await users.to_list(length=None)

    async def get_remaining_time(self, user_id):
        user = await self.col.find_one({'_id': int(user_id)})
        if user and user.get('is_prime', False):
            prime_expiry = user.get('prime_expiry', None)
            if prime_expiry:
                remaining_time = prime_expiry - datetime.utcnow()
                if remaining_time.total_seconds() > 0:
                    return remaining_time
        return None

    async def get_prime_membership_price(self, duration: str):
        prices = {
            '7d': 10,
            '1m': 20
        }
        return prices.get(duration, None)

# Initialize the database
AshutoshGoswami24 = Database(Config.DB_URL, Config.DB_NAME)
