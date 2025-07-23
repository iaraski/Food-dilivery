import { getUserById } from '@/entities/user/api';

export default async function UserPage({ params }: { params: { id: string } }) {
  let user;

  try {
    user = await getUserById(params.id);
  } catch (error) {
    console.error(error);
    return <div>Ошибка загрузки пользователя</div>;
  }

  return (
    <div>
      <h1>Профиль</h1>
      <p>почта:{user.email}</p>
      <p>имя:{user.name}</p>
      <p>пароль:{user.password}</p>
    </div>
  );
}
