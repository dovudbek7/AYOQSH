let d = document.querySelector('.i')


function cl() {
    let inp = document.querySelector('.inpp').value 
    if (inp.toLowerCase() == 'english') {
        d.innerHTML = 
            `
            <input type="text">
            <input type="text">
            <input type="text">
            <input type="text">
            <input type="text">
            `
    }
}
