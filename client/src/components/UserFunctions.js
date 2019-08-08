import axios from 'axios'

export const register = newUser => {
    return axios
        .post("/register", {
            // first_name: newUser.first_name,
            // last_name: newUser.last_name,
            username: newUser.username,
            password: newUser.password
        })
        .then(response => {
            console.log("Registered")
        })
}

export const login = user => {
    return axios
        .post("/auth", {
            username: user.username,
            password: user.password
        })
        .then(response => {
            localStorage.setItem('usertoken', response.data.token)
            return response.data.token
        })
        .catch(err => {
            console.log(err)
        })
}