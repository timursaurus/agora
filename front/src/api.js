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

const HTTP = axios.create({
    baseURL: baseURL,
    timeout: 5000,
    // headers: { Authorization: `Bearer ${store.state.accessToken}` },
})


export default HTTP