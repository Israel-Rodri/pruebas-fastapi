import axios from 'axios';

const API_BASE_URL = 'http://localhost:3000' || 'http://127.0.0.1:3000'

const api = axios.create({
    baseURL: API_BASE_URL,
    headers: {
        'Content-Type':'application/json',
    },
    timeout: 10000,
});

api.interceptors.response.use(
    (response) => response,
    (error) => {
        console.error('Error en la peticion:', error);
        return Promise.reject(error)
    }
);

export default api