function showSelectedOptions() {
    var inp = document.getElementById("inp");
    var fromCurrency = document.getElementById("fromCurrency");
    var toCurrency = document.getElementById("toCurrency");

    // Manually check if the required fields are filled
    if (inp.value.trim() === "") {
        alert("Please enter a value in the Amount field.");
        return;
    }

    if (fromCurrency.value.trim() === "") {
        alert("Please select a currency in the From field.");
        return;
    }

    if (toCurrency.value.trim() === "") {
        alert("Please select a currency in the To field.");
        return;
    }

    // Create a form dynamically
    var form = document.createElement("form");
    form.setAttribute("method", "post");
    form.setAttribute("action", "/convert");

    // Append input fields
    form.appendChild(createHiddenInput("inp", inp.value));
    form.appendChild(createHiddenInput("fromCurrency", fromCurrency.value));
    form.appendChild(createHiddenInput("toCurrency", toCurrency.value));

    // Append the form to the document and submit it
    document.body.appendChild(form);
    form.submit();
}

function createHiddenInput(name, value) {
    var input = document.createElement("input");
    input.setAttribute("type", "hidden");
    input.setAttribute("name", name);
    input.setAttribute("value", value);
    return input;
}

document.addEventListener("DOMContentLoaded", function () {
    const convertButton = document.getElementById("convertButton");
    convertButton.addEventListener("click", showSelectedOptions);
});
