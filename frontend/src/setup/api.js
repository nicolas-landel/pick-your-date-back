
import axios from "axios";


console.log("ENNNNV", import.meta.env.VITE_API_URL)

const API = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
  headers: {
    "Content-type": "application/json"
  },
});

class APIService {
  get(path) {
    return API.get(path)
  }
  post(path, data) {
    return API.post(path, data)
  }
}

export default new APIService();