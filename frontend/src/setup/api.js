import axios from "axios";


console.log("ENNNNV", process.env.VUE_APP_API_URL)

const API = axios.create({
  baseURL: process.env.VUE_APP_API_URL,
  headers: {
    "Content-type": "application/json"
  },
});

class APIService {
  get(path) {
    return API.get(path)
  }
}

export default new APIService();