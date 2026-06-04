/* jshint esversion: 11 */
/* global bootstrap */

let options = document.getElementsByClassName("option");

for (let option of options) {
    option.addEventListener("click", (e) => {
        let userOption = e.currentTarget;
        let name = userOption.dataset.name;
        let description = userOption.dataset.description;
        let unit_price = userOption.dataset.price;
        let delivery = userOption.dataset.delivery;

        let optionName = document.getElementById("option-name");
        optionName.innerText = `${name}`;

        let optionDescription = document.getElementById("option-description");
        optionDescription.innerText = `${description}`;
       
        let optionPrice = document.getElementById("option-price");
        optionPrice.innerText = `Price: $${unit_price}`;

        let optionPk = document.getElementById("selected-option-pk");
        optionPk.value = userOption.dataset.pk;

        let deliveryDays = document.getElementById("delivery-days");
         
        if(name === "Set Up Service"){
            deliveryDays.classList.remove("d-none");
            deliveryDays.innerText = `Once access is arranged, your system is set up and delivered within ${delivery} working day(s).`; 
        } else if (name === "DIY Template"){
            deliveryDays.classList.add("d-none");
        }
});
}

const button = document.getElementById("add-basket");
const loginPrompt = document.getElementById("login-prompt");
const loginPromptModal = new bootstrap.Modal(loginPrompt);

if (button){
    button.addEventListener("click", (e) => {
    e.preventDefault();
    loginPromptModal.show();
});
}







