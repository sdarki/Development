const BASE_URL ="https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies";
const dropdowns=document.querySelectorAll(".dropdown select");
 const btn=document.querySelector("form button");
const fromCurr=document.querySelector(".from select");
const toCurr=document.querySelector(".to select");
const apiKey="285cce8f1367e9331b15dc80";
for(code in countryList){
    console.log(code,countryList[code]);
}
for(let select of dropdowns){
    for(const currCode in countryList){
        const newOption=document.createElement("option");
        newOption.innerText=currCode;
        newOption.value=currCode;
        select.append(newOption);
    }
    select.addEventListener("change",(event)=>{
        updateFlag(event.target);
    });
}
const updateFlag=(element)=>{
    let current=element.value;
    let countryCode=countryList[current];
    let newsrc=`https://flagsapi.com/${countryCode}/flat/64.png`;
    let flags=element.parentElement.querySelector("img");
    flags.src=newsrc;
}
 btn.addEventListener("click",async(e)=>{
    e.preventDefault();
    let amount=document.querySelector(".amount input");
    let amtVal=amount.value;
    if(amtVal==="" || amtVal<1){
        amtVal=1;
        amount.value="1";
    }
    let url=`https://v6.exchangerate-api.com/v6/${apiKey}/latest/${fromCurr.value}`;
    let response=await fetch(url);
   let json=await response.json();
   let exchangeRate=json.conversion_rates[toCurr.value];
   let totalExchangeRate=(amtVal*exchangeRate).toFixed(2);
   const exchangeRateTxt=document.querySelector(".result");
   exchangeRateTxt.innerText=totalExchangeRate;
 })