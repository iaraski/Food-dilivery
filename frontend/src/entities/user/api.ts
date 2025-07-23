import { User } from './model';

const API_Base = 'http://localhost:8000/api';

export async function getUserById(id: string): Promise<User> {
  const res = await fetch(`${API_Base}/users/${id}`, {
    method: 'GET',
    headers: {
      'Content-type': 'application/json',
    },
  });
  if (!res.ok) {
    throw new Error('Failed to fetch user');
  }
  return res.json();
}
