const stripePublicKey = document.getElementById('id_stripe_public_key')
    .innerText.slice(1, -1);

const clientSecret = document.getElementById('id_client_secret')
    .innerText.slice(1, -1);

const stripe = Stripe(stripePublicKey);

const elements = stripe.elements();

const style = {
    base: {
        color: '#0F172A',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#475569'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};

const card = elements.create('card', { style: style });
card.mount('#card-element');

// Display error message
card.addEventListener('change', function (e) {
    const errorDiv = document.getElementById('card-errors');

    if (e.error) {
        const html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${e.error.message}</span>
        `;
        errorDiv.innerHTML = html;
    } else {
        errorDiv.textContent = '';
    }
});