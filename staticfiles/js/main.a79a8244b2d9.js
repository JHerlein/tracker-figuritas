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
    textToAdd.cols = '100'
    textToAdd.rows = '5'
    textToAdd.innerText = message
    
    if(textAreaLength < 1){
        divText[0].append(textToAdd)
    }    
    
}

function ShowFilters(e){    
    table = document.getElementById('main-table')
    table.classList = "col-9 mt-4 ms-2 pt-lg-2"
}
