from django.core.management.base import BaseCommand
from services.models import WebFeature

features = [
    ['Static Site', 'Fast, secure website with fixed content—ideal for businesses needing a reliable online presence with minimal maintenance.'],

    ['Mobile Optimization (Responsive Design)', 'Fully responsive design that ensures your website looks and works perfectly on mobile, tablet, and desktop devices.'],

    ['Deployment & Hosting Setup', 'Complete setup and deployment of your website, including domain connection and hosting configuration for a smooth launch.'],

    ['Custom Email', 'Professional branded email addresses (e.g., info@yourdomain.com) to enhance credibility and business communication.'],

    ['Base Blog', 'Built-in blog system to publish articles, updates, and content that helps engage visitors and improve SEO.'],

    ['E-Commerce', 'Online store functionality with product listings, shopping cart, and secure checkout to sell products or services directly.'],

    ['Copyright Protection', 'Basic content protection measures to help prevent unauthorized copying of your website’s text and media.'],

    ['Hiring & Vacancy', 'Dedicated careers or jobs page where you can post openings and receive applications from candidates.'],

    ['SEO Optimization', 'Search engine–friendly structure including meta tags, proper headings, and indexing setup to improve visibility on Google.'],

    ['Specialized User-end Performance Optimization (like caching and service workers)', 'Advanced performance enhancements such as caching and service workers for faster load times and smoother user experience.'],

    ['Ordering & Reservation', 'Integrated booking or ordering system with forms or scheduling tools for appointments, services, or reservations.'],

    ['Specialized UI/UX Design', 'Custom-designed user interface focused on usability, branding, and converting visitors into customers.'],

    ['Analytics & Tracking', 'Integration of analytics tools to track visitor behavior, traffic sources, and website performance insights.'],
]

class Command(BaseCommand):
    help = 'Populate Features'

    def handle(self, *args, **options):
        for feature in features:
            a = WebFeature(name=feature[0])
            if feature[1]:
                a.description = feature[1]
            a.value = 4
            a.save()

        self.stdout.write('Populating Successful')