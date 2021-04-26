import axios from 'axios'

const baseURL = 'http://localhost:8080/api/'

let req = {
    baseURL: baseURL,
    timeout: 5000,
    headers: {
		Authorization: localStorage.getItem('access_token')
			? 'JWT ' + localStorage.getItem('access_token')
			: null,
		'Content-Type': 'application/json',
		accept: 'application/json',
	},

}

export const HTTP = axios.create(req)