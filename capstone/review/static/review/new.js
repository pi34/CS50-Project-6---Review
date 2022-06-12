document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('#review-form').onsubmit = () => {
        const title = document.querySelector('#review-title').value
        const rating = document.querySelector('#review-rating').value
        const body = document.querySelector('#review-body').value
        const id = document.querySelector('#review-form').name
        fetch(`/review/${id}`, ({
            method: 'POST', 
            body: JSON.stringify({
                title: title, 
                rating: rating, 
                body: body
            })
        }))
    }
})