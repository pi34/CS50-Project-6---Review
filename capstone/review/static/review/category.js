document.addEventListener('DOMContentLoaded', function() {

    document.addEventListener('click', event => {
        const element = event.target

        if (element.classList.contains('like')) {
            fetch (`/business/${element.value}`, {
                method: 'PUT',
                body: JSON.stringify({})
            })
            .then(location.reload())
        } 
        
        else if (element.classList.contains("edit")) {
            document.querySelector(`#p_${element.parentElement.id}`).contentEditable = "true"
            save = document.createElement('button')
            save.innerHTML = "Save"
            save.classList.add("btn-outline-success", "btn", "save")
            element.parentElement.append(save)
            element.disabled = "true"
        } 
        
        else if (element.classList.contains("save")) {
            body = document.querySelector(`#p_${element.parentElement.id}`).innerHTML
            edit_page(element.parentElement.id, body)
            body.contentEditable = "false"
            element.remove()
            document.querySelectorAll('.edit').disabled = "false"
        }
    })

    fetch ('/category')
    .then (response => response.json())
    .then (categories => {
        categories.categories.forEach(category => {
            let item = document.createElement('a')
            item.innerHTML = category
            item.href = `/all/${category}`
            item.id = category
            item.classList.add("dropdown-item", "category")
            document.querySelector('#categories').append(item)
        })
    })
 

})


function edit_page(id, body) {
    fetch(`/business/${id}`, {
        method: 'PUT', 
        body: JSON.stringify({
            body: body
        })
    })
    .then (location.reload())
}