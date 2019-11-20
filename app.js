// CACHING THE DOM
const mainForm = document.getElementById('main-form');
const formInput = document.getElementById('name-input');
const output = document.getElementById('output');

// ADD EVENT LISTENER TO MAIN-FORM
mainForm.addEventListener('submit', getData);

class Access {
    constructor(accessName) {
        this.accessName = accessName;
        const data = '';
    }

    fetchData() {
        fetch('./database.json')
        .then((res) => res.json())
        .then(dataRes => this.data = dataRes)
        .catch(err => console.log(err));
    }

    displayData() {
        console.log(this.data);
    }
}

function getData(e) {
    e.preventDefault();

    const newAccess = new Access(formInput.value);
    newAccess.fetchData();
    newAccess.displayData();
}



