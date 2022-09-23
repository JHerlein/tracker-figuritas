function createExchangeMessage() {

    let divText = document.getElementsByClassName('text-message')
    let stickers = document.getElementsByClassName('sticker-item')
    let textAreaLength = document.getElementsByTagName('textarea').length
    let message =  'Figuritas a cambiar: '

    for (let i = 0; i < stickers.length; i++){        
        let messageToAdd = stickers[i].textContent + ' '  
        message += messageToAdd
    }
    
    let textToAdd = document.createElement('textarea')
    textToAdd.cols = '50'
    textToAdd.rows = '5'
    textToAdd.innerText = message
    
    if(textAreaLength < 1){
        divText[0].append(textToAdd)
    }    
    
}

function ShowFilters(e){    
    table = document.getElementById('main-table')
    filters = document.getElementsByClassName('filter-list')        
    if(table.classList.value === "col-4 mt-2 ms-2"){        
        filters[0].classList.toggle("invisible")
        filters[1].classList.toggle("invisible")
        table.classList.value = "col-11 mt-2 ms-2"
        e.innerText = "Mostrar Filtros"
    }
    else if (table.classList.value === "col-11 mt-2 ms-2"){
        filters[0].classList.toggle("invisible")
        filters[1].classList.toggle("invisible")        
        table.classList.value = "col-4 mt-2 ms-2"
        e.innerText = "Ocultar Filtros"
    }
    
    
}
