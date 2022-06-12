// Start with first post
let counter = 1;

// When DOM loads, render the first 20 posts
document.addEventListener('DOMContentLoaded', load);

// If scrolled to bottom, load the next 20 posts
window.onscroll = () => {
    if (window.innerHeight + window.scrollY >= document.body.offsetHeight) {
        load();
    }
};

// Load next set of posts
function load() {

    // Set start and end post numbers, and update counter
    const start = counter;
    counter++

    const location = document.querySelector('#location')

    let query = null

    if (location != undefined) {
        query = location.innerHTML
    }

    fetch(`/reviews/${document.querySelector('#type').innerHTML}?start=${start}&location=${query}`)
    .then(response => response.json())
    .then(data => {
        data.forEach(add_post);
    })
};

// Add a new post with given contents to DOM
function add_post(contents) {

    const post = document.createElement('div');
    // Create new post
    if (document.querySelector('#type').value == 'review') {
        post.innerHTML = `<div class="card">
        <div class="card-body">
        <h5 class="card-title">${contents.title}</h5>
        <p class="card-text">${contents.body}</p>
        <a href="/business/${contents.business_id}" class="btn btn-primary">Visit ${contents.business_name}</a>
        <button value=${contents.id} id="l_${contents.id}" class="btn like"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-heart-fill like" viewBox="0 0 16 16">
            <path class="like" fill-rule="evenodd" d="M8 1.314C12.438-3.248 23.534 4.735 8 15-7.534 4.736 3.562-3.248 8 1.314z"/>
        </svg></button> ${contents.likes.length} likes
        </div>`

        document.querySelector('#review-section').append(post);


        const username = document.querySelector('#profile-name')

        if (username) {
            if (contents.likes.indexOf(username.innerHTML) !== -1) {  
                document.querySelector(`#l_${contents.id}`).style.color = "black"
            } else {
                document.querySelector(`#l_${contents.id}`).style.color = "red"
            }

        if (contents.user === username.innerHTML) {
            document.querySelector(`#l_${contents.id}`).remove()
        } 
            
        } else {
            document.querySelectorAll('.edit').forEach(element => {element.remove()})
            document.querySelectorAll('.like').forEach(element => {element.remove()})
        }

    } else if (document.querySelector('#type').value == 'business') {
        post.innerHTML = `<div class="card-deck">
        <div class="card" style="width: 18rem;">
          <div class="card-body">
            <h5 class="card-title">${contents.name}</h5>
            <p class="card-text">${contents.body}</p>
            <a href='/business/${contents.id}' class="btn btn-primary">See More</a>
          </div>
        </div>
      </div>`

      document.querySelector('#review-section').append(post);
    };
    }

    