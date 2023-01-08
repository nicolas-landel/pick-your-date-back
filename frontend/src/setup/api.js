
import axios from "axios";
import { TokenService } from "./tokenService";

const API = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
  headers: {
    "Content-type": "application/json",
    "Authorization": `Token ${TokenService.getToken()}`
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