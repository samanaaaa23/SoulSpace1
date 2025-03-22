import axios from "axios";
import Cookies from "js-cookie";

const API_URL = "http://127.0.0.1:8000/api";

export const login = async (username: string, password: string) => {
    try {
        const response = await axios.post(`${API_URL}/login/`, {
            username,
            password,
        });

       
        Cookies.set("access", response.data.access, { expires: 1 });
        Cookies.set("refresh", response.data.refresh, { expires: 7 });

        return response.data;
    } catch (error) {
        throw new Error("Invalid username or password");
    }
};

export const getUser = async () => {
    const accessToken = Cookies.get("access");
    if (!accessToken) return null;

    try {
        const response = await axios.get(`${API_URL}/user/`, {
            headers: { Authorization: `Bearer ${accessToken}` },
        });
        return response.data;
    } catch (error) {
        return null;
    }
};

export const logout = () => {
    Cookies.remove("access");
    Cookies.remove("refresh");
};