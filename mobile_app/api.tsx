import axios from 'axios';
import { Product } from './types';

const fetchProducts = async (): Promise<Product[]> => {
    return axios
        .get('http://localhost:8000');
}