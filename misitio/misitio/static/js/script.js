const currentDate = document.querySelector(".current-date"),
daysV = document.querySelector(".days"),
PreviaSiguienteIcon = document.querySelectorAll(".icons span");

let date = new Date(),
Year = date.getFullYear(),
Month = date.getMonth();

console.log(date, Year, Month);

const months =  ["Enero", "Febrero", "Marzo", "Abril",
                 "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
const renderCalendar = () => {
    let primerDiaMes = new Date(Year, Month, 1).getDay(),
    ultimoDiaMes = new Date(Year, Month + 1,0).getDate(); //ULTIMO DIA DEL MES
    let dayPlaceholder = ``;
    
    console.log(ultimoDiaMes);
    for(let i = primerDiaMes; i > 0; i--){
        dayPlaceholder += `<li class = "inactive" >${i}</li>`;
    }
    for(let i = 1; i <= ultimoDiaMes; i++){
        dayPlaceholder += `<li> ${i} </li>`;
    }
    currentDate.innerText =  `${months[Month]} ${Year}`;
    daysV.innerHTML = dayPlaceholder;
}

renderCalendar();

PreviaSiguienteIcon.forEach(icon => {
    icon.addEventListener("click", () => {
        console.log(icon);
        icon.id === "Previa" ? console.log(Month-1) : console.log(Month + 1);
        Month = icon.id === "Previa" ? Month - 1 : Month + 1;
        renderCalendar();
    });
});