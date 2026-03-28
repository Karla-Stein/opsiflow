let options = document.getElementsByClassName("option")
let description = document.getElementsByClassName("option-description")

for (let option of options) {
    option.addEventListener("click", (e) => {
        e.preventDefault();
        userOption = e.target.innerText;
        let name = option.dataset.name;
        let description = option.dataset.description;
        let unit_price = option.dataset.price;
        let delivery = option.dataset.delivery;

        let optionName = document.getElementById("option-name");
        optionName.innerText = `${name}`

        let optionDescription = document.getElementById("option-description");
        optionDescription.innerText = `${description}`
       
        let optionPrice = document.getElementById("option-price");
        optionPrice.innerText = `Price: $${unit_price}`;

        let deliveryDays = document.getElementById("delivery-days");
         deliveryDays.innerText = `Once access is arranged, your system is set up and delivered within ${delivery} working days.`
        if(userOption === "Set Up Service"){
           deliveryDays.classList.remove("d-none")
        } else if (userOption === "DIY Template"){
            deliveryDays.classList.add("d-none")
        };
});
}

const button = document.getElementById("add-basket")
const loginPrompt = document.getElementById("login-prompt")
const loginPromptModal = new bootstrap.Modal(loginPrompt);

button.addEventListener("click", (e) => {
    e.preventDefault();
    loginPromptModal.show();
});







