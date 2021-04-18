import axios from 'axios'

let req = {
    baseURL: 'http://localhost:8080/'
}

export const HTTP = axios.create(req)