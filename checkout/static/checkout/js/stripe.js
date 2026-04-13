const stripePublicKey = document.getElementById('id_stripe_public_key')
    .innerText.slice(1, -1);

const clientSecret = document.getElementById('id_client_secret')
    .innerText.slice(1, -1);

const stripe = Stripe(stripePublicKey);
// Stripe payment element
const appearance = { /* appearance */ };
const options = {
  layout: {
    type: 'accordion',
    defaultCollapsed: false,
    radios: 'always',
    spacedAccordionItems: false
  }
};

const elements = stripe.elements({ clientSecret, appearance });
const paymentElement = elements.create('payment', options);
paymentElement.mount('#payment-element');

const form = document.getElementById('payment-form');
const submitButton = document.getElementById('submit-button');

// CSRF protection for AJAX POST request to django
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

form.addEventListener('submit', async (event) => {
    event.preventDefault();

    submitButton.disabled = true;
    // Send form data to Django before payment confirmation
    const formData = new FormData(form);
    const csrftoken = getCookie('csrftoken');
    const response = await fetch('/checkout/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrftoken,
        },
        body: formData,
    });
    if (!response.ok) {
        throw new Error('Could not save checkout data.');
    }
    const data = await response.json();
    
    // Awaiting payment confirmation and redirect to success page
    const {error} = await stripe.confirmPayment({
    //`Elements` instance that was used to create the Payment Element
        elements,
        confirmParams: {
        return_url: window.location.origin + '/checkout/success/'
    },
  });

  if (error) {
    // This point will only be reached if there is an immediate error when
    // confirming the payment. Show error to your customer (for example, payment
    // details incomplete)
    const messageContainer = document.querySelector('#payment-errors');
    messageContainer.textContent = error.message;
  }
});

// Display error message
paymentElement.addEventListener('change', function (e) {
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