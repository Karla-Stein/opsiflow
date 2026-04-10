const stripePublicKey = document.getElementById('id_stripe_public_key')
    .innerText.slice(1, -1);

const clientSecret = document.getElementById('id_client_secret')
    .innerText.slice(1, -1);

const stripe = Stripe(stripePublicKey);

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


// const elements = stripe.elements();

// const style = {
//     base: {
//         color: '#0F172A',
//         fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
//         fontSmoothing: 'antialiased',
//         fontSize: '16px',
//         '::placeholder': {
//             color: '#475569'
//         }
//     },
//     invalid: {
//         color: '#dc3545',
//         iconColor: '#dc3545'
//     }
// };

// const card = elements.create('card', { style: style });
// card.mount('#card-element');

// Display error message
// paymentElement.addEventListener('change', function (e) {
//     const errorDiv = document.getElementById('card-errors');

//     if (e.error) {
//         const html = `
//             <span class="icon" role="alert">
//                 <i class="fas fa-times"></i>
//             </span>
//             <span>${e.error.message}</span>
//         `;
//         errorDiv.innerHTML = html;
//     } else {
//         errorDiv.textContent = '';
//     }
// });

// const form = document.getElementById('payment-form');
// const submitButton = document.getElementById('submit-button');

//  Handle form submit
// form.addEventListener('submit', function (e) {
//     e.preventDefault();

//     paymentElement.update({ disabled: true });
//     submitButton.disabled = true;

//     stripe.confirmCardPayment(clientSecret, {
//         payment_method: {
//             card: card,
//         }
//     }).then(function (result) {
//         if (result.error) {
//             const errorDiv = document.getElementById('card-errors');

//             const html = `
//                 <span class="icon" role="alert">
//                     <i class="fas fa-times"></i>
//                 </span>
//                 <span>${result.error.message}</span>
//             `;

//             errorDiv.innerHTML = html;

//             paymentElement.update({ disabled: false });
//             submitButton.disabled = false;
//         } else {
//             if (result.paymentIntent.status === 'succeeded') {
//                 form.submit();
//             }
//         }
//     });
// });

// Handle payment form submit 
const form = document.getElementById('payment-form');
const submitButton = document.getElementById('submit-button');

form.addEventListener('submit', async (event) => {
    event.preventDefault();

    submitButton.disabled = true;

    const {error} = await stripe.confirmPayment({
    //`Elements` instance that was used to create the Payment Element
        elements,
        confirmParams: {
        return_url: window.location.origin + '/',
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