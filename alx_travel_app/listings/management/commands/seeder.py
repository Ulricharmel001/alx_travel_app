from django.core.management.base import BaseCommand
from listings.models import Listing, Booking, Review
from django.contrib.auth.models import User
from faker import Faker
import random
from datetime import timedelta, date

class Command(BaseCommand):
    help = 'Seed the database with sample listings, bookings, and reviews'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Create sample users
        users = []
        for _ in range(100):
            user = User.objects.create_user(
                username=fake.user_name(),
                email=fake.email(),
                password='password123'
            )
            users.append(user)

        # Create sample listings
        listings = []
        for _ in range(1000):
            listing = Listing.objects.create(
                title=fake.sentence(nb_words=6),
                description=fake.paragraph(nb_sentences=3),
                price_per_night=random.uniform(50, 500),
                location=fake.city()
            )
            listings.append(listing)

        # Create sample bookings
        for _ in range(1000):
            listing = random.choice(listings)
            user = random.choice(users)
            start_date = fake.date_between(start_date='-30d', end_date='+30d')
            end_date = start_date + timedelta(days=random.randint(1, 14))
            total_price = listing.price_per_night * (end_date - start_date).days

            Booking.objects.create(
                listing=listing,
                user=user,
                start_date=start_date,
                end_date=end_date,
                total_price=total_price
            )

        # Create sample reviews
        for _ in range(40):
            listing = random.choice(listings)
            user = random.choice(users)
            rating = random.randint(1, 5)
            comment = fake.paragraph(nb_sentences=2)

            Review.objects.create(
                listing=listing,
                user=user,
                rating=rating,
                comment=comment
            )

        self.stdout.write(self.style.SUCCESS('Database seeded successfully!'))
