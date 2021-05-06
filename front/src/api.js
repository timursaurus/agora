import axios from 'axios'
// import store from '@/store'

const baseURL = 'http://127.0.0.1:8000/'

// const HTTP = axios.create({
//     baseURL: baseURL,
//     timeout: 5000,
//     headers: {
// 		Authorization: localStorage.getItem('access_token')
// 			? 'JWT ' + localStorage.getItem('access_token')
// 			: null,
// 		'Content-Type': 'application/json',
// 		accept: 'application/json',
// 	},
// })
// if (localStorage.getItem('accessToken'))

const HTTP = axios.create({
    baseURL: baseURL,
    timeout: 5000,
    headers: { Authorization: `Bearer ` + localStorage.getItem('accessToken') },
})

HTTP.interceptors.response.use((res) => {
    return res
    },
    async function (err) {
        const originalRequest = err.config

        if (typeof err.response === 'undefined') {
            // alert('Network error')
            return Promise.reject(err)

        }
        if (err.response.data.code === 'token_not_valid' &&
            err.response.status === 401 &&
            err.response.statusText === 'Unauthorized') {
            
                const refreshToken = localStorage.getItem('refreshToken')
                const tokenParts = JSON.parse(atob(refreshToken.split('.')[1]))
                const now = Math.ceil(Date.now() / 1000)

                if (tokenParts.exp > now) {
                    return HTTP.post('api/token/refresh')
                        .then((res) => {
                            localStorage.setItem('accessToken', res.data.access)
                            localStorage.setItem('refreshToken', res.data.refresh)

                            HTTP.defaults.headers['Authorization'] = 'Bearer ' + res.data.access
                            originalRequest.headers['Authorization'] = 'Bearer ' + res.data.access

                            return HTTP(originalRequest)
                        }).catch((err) => console.log(err))
                } else {
                    window.location.href = '/signin'
                }
        } else {
            window.location.href = '/signin'
        }

    } 


)

export default HTTP