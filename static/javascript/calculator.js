// Initialize variables to store total weight and value for each scrap type
var aluminumWeight = 0;
var aluminumValue = 0;
var brassWeight = 0;
var brassValue = 0;
var copperWeight = 0;
var copperValue = 0;
var stainlessSteelWeight = 0;
var stainlessSteelValue = 0;
var paperWeight = 0;
var paperValue = 0;
var cardboardWeight = 0;
var cardboardValue = 0;
var plasticWeight = 0;
var plasticValue = 0;
var ironWeight = 0;
var ironValue = 0;

// Define function to calculate scrap price
function calculatePrice() {
  // Get input values
  var weight = parseFloat(document.getElementById("weight").value);
  var scrapType = document.getElementById("scrap-type").value;
  
  // Calculate price based on scrap type
  var pricePerKg;
  switch(scrapType) {
    case "aluminum":
      pricePerKg = 105;
      // Update total weight and value for aluminum
      aluminumWeight += weight;
      aluminumValue += weight * pricePerKg;
      break;
    case "brass":
      pricePerKg = 300;
      // Update total weight and value for brass
      brassWeight += weight;
      brassValue += weight * pricePerKg;
      break;
    case "copper":
      pricePerKg = 425;
      // Update total weight and value for copper
      copperWeight += weight;
      copperValue += weight * pricePerKg;
      break;
    case "stainless-steel":
      pricePerKg = 37;
      // Update total weight and value for stainless steel
      stainlessSteelWeight += weight;
      stainlessSteelValue += weight * pricePerKg;
      break;
      case "paper":
        pricePerKg = 18;
        // Update total weight and value for paper
        paperWeight += weight;
        paperValue += weight * pricePerKg;
        break;
      case "cardboard":
        pricePerKg = 10;
        // Update total weight and value for cardboard
        cardboardWeight += weight;
        cardboardValue += weight * pricePerKg;
        break;
      case "plastic":
        pricePerKg = 10;
        // Update total weight and value for plastic
        plasticWeight += weight;
        plasticValue += weight * pricePerKg;
        break;
      case "iron":
        pricePerKg = 30;
        // Update total weight and value for iron
        ironWeight += weight;
        ironValue += weight * pricePerKg;
        break;
    default:
      pricePerKg = 0;
  }
  
  // Calculate total price
  var totalPrice = weight * pricePerKg;
  
  // Display result
  document.getElementById("total-price").innerHTML = "₹" + totalPrice.toFixed(2);
  
  // Calculate additional price
  var additionalPrice = 0;
  var additionalType = document.getElementById("additional-type").value;
  if (additionalType === "hazardous") {
    additionalPrice = 0.25;
  } else if (additionalType === "large-quantity") {
    additionalPrice = 0.50;
  }
  
  // Display additional price
  document.getElementById("additional-price").innerHTML = "₹" + (weight * additionalPrice).toFixed(2);
  
  // Display total weight and value for each metal type
  document.getElementById("aluminum-weight").innerHTML = aluminumWeight.toFixed(2) + " Kg";
  document.getElementById("aluminum-value").innerHTML = "₹" + aluminumValue.toFixed(2);
  document.getElementById("brass-weight").innerHTML = brassWeight.toFixed(2) + " Kg";
  document.getElementById("brass-value").innerHTML = "₹" + brassValue.toFixed(2);
  document.getElementById("copper-weight").innerHTML = copperWeight.toFixed(2) + " Kg";
  document.getElementById("copper-value").innerHTML = "₹" + copperValue.toFixed(2);
  document.getElementById("stainless-steel-weight").innerHTML = stainlessSteelWeight.toFixed(2) + " Kg";
  document.getElementById("stainless-steel-value").innerHTML = "₹" + stainlessSteelValue.toFixed(2);
  document.getElementById("paper-weight").innerHTML = paperWeight.toFixed(2) + " Kg";
  document.getElementById("paper-value").innerHTML = "₹" + paperValue.toFixed(2);document.getElementById("cardboard-weight").innerHTML = cardboardWeight.toFixed(2) + " Kg";
  document.getElementById("cardboard-value").innerHTML = "₹" + cardboardValue.toFixed(2);
  document.getElementById("plastic-weight").innerHTML = plasticWeight.toFixed(2) + " Kg";
  document.getElementById("plastic-value").innerHTML = "₹" + plasticValue.toFixed(2);
  document.getElementById("iron-weight").innerHTML = ironWeight.toFixed(2) + " Kg";
  document.getElementById("iron-value").innerHTML = "₹" + ironValue.toFixed(2);
}

// Attach click event to calculate button
document.getElementById("calculate-btn").addEventListener("click", calculatePrice);