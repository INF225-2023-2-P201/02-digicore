import React, { useState } from 'react';
import { useForm } from 'react-hook-form';
import { createSetting } from '../api/digicore.api';

export function SettingsPage() {
  const { register, handleSubmit, formState: { errors } } = useForm();
  const [customError, setCustomError] = useState('');

  const onSubmit = handleSubmit(async (data) => {
    const re = /Denegar\s+el\s+acceso\s+de\s+(PC1|A|PC2|B)\s+a\s+internet/;
    if (re.test(data.input)) {
      const res = await createSetting(data);
      console.log(res);
      if (res['message'] === 'Command not found') {
        setCustomError('El lenguaje utilizado no cumple con lo establecido en instrucciones.');
      } else {
        setCustomError('');
      }
    } else {
      setCustomError('El lenguaje utilizado no cumple con lo establecido en instrucciones.');
    }
  });

  return (
    <div className="max-w-xl mx-auto my-auto mt-28">
      <form onSubmit={onSubmit} className="text-center flex flex-col items-center">
        <h2 className="font-bold text-4xl mb-4">Generador de Comandos</h2>
        <textarea
          placeholder="Ingrese su intención"
          cols="70"
          rows="10"
          {...register("input", { required: true })}
          className="bg-zinc-700 p-3 rounded-lg block w-full h-50 mb-3"
        ></textarea>
        {errors.input && (<span className="text-red-100 bg-red-500 text-sm font-bold py-1 px-2 rounded">Este campo es requerido</span>)}
        {customError && (<span className="text-red-100 bg-red-500 text-sm font-bold py-1 px-2 rounded">{customError}</span>)}

        <div className="flex w-full justify-between mt-3">
          <button className="bg-violet-500 hover:bg-violet-700 p-3 rounded-lg flex-1">Enviar</button>
          <span className="bg-violet-500 hover:bg-violet-700 p-3 rounded-lg flex-1 ml-2 cursor-pointer">Instrucciones</span>
        </div>
      </form>
    </div>
  );
}
