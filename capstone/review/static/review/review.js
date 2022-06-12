document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('#new').onsubmit = () => {
        const name = document.querySelector('#input-name').value
        const address = document.querySelector('#input-address').value
        const bio = document.querySelector('#input-bio').value
        const image = document.querySelector('#input-image').files[0].name
        fetch('/new', ({
            method: 'POST', 
            body: JSON.stringify({
                name: name,
                address: address, 
                description: bio,
                image: image
            }) 
        }))
    }
})