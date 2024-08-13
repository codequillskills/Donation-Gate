# DonationGate Project

## Overview

**DonationGate** is a web-based platform built using Django, designed to facilitate online donations for various causes. The application integrates Razorpay as its payment gateway to ensure secure and efficient transactions.

## Features

- **Homepage**: A simple landing page for your donation platform.
- **Details Page**: Collects donor details such as name, email, phone number, and donation amount.
- **Donation Page**: Processes payments through Razorpay and handles the transaction securely.
- **Success Page**: Confirms successful payments.
- **Failure Page**: Handles and informs users about failed transactions.

## Prerequisites

- Python 3.8+
- Django 3.2+
- Razorpay API Key and Secret

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/codequillskills/Donation-Gate
   cd Donation-Gate
   ```

2. **Set Up the Virtual Environment**

   ```bash
   python -m venv donationgate
   .\donationgate\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**

   Create a `.env` file in the root directory of your project with the following content:

   ```bash
   SECRET_KEY=your_django_secret_key
   DEBUG=False
   ALLOWED_HOSTS=localhost,127.0.0.1,yourdomain.com
   RAZORPAY_KEY_ID=your_razorpay_key_id
   RAZORPAY_KEY_SECRET=your_razorpay_key_secret
   ```

5. **Apply Migrations**

   Even though there are no models, run the following command to ensure all necessary Django tables are created:

   ```bash
   python manage.py makemigrations && python manage.py migrate
   ```

6. **Run the Development Server**

   ```bash
   python manage.py runserver
   ```

7. **Access the Application**

   Open your web browser and go to `http://127.0.0.1:8000`.

## Razorpay Integration

The donation process is handled through Razorpay. In the `donatepage` view:

- A payment order is created using Razorpay's API.
- The amount is calculated in paisa (₹1 = 100 paisa).
- The payment form is rendered with Razorpay's payment button.

## Templates

- **`homepage.html`**: The landing page for the application.
- **`detailspage.html`**: The form where users provide their donation details.
- **`donatepage.html`**: Contains the Razorpay payment button and order details.

## Contributing

Feel free to fork the project, make changes, and submit a pull request. Contributions are welcome!

## License

This project is licensed under the MIT License.
