document.addEventListener('DOMContentLoaded', function () {
    if (document.querySelector('#follow')) {
        document.querySelector('#follow').addEventListener('click', () => {
            let user = document.querySelector('#username').innerHTML
            console.log(user)
            fetch(`/profile/${user}`, {
                method: 'PUT'
            })
            .then(location.reload())
        })
    }
})