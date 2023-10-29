import { Link, useLocation } from 'react-router-dom';

export function Navigation() {
  const location = useLocation();

  return (
    <div className='flex justify-between py-3'>
        <Link to='/create'>
            <h1 className='font-bold text-3xl mb-4'>DigiCore</h1>
        </Link>
        {location.pathname === '/create' ? (
          <button className='bg-violet-500 hover:bg-violet-700 px-3 py-2 rounded-lg'>
            <Link to='/history'>Historial</Link>
          </button>
        ) : (
          <button className='bg-violet-500 hover:bg-violet-700 px-3 py-2 rounded-lg'>
            <Link to='/create'>Crear Regla</Link>
          </button>
        )}
    </div>
  );
}

