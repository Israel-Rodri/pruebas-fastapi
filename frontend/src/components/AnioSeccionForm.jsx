//Importar el hook useState para poder controlar cambios en el form
import { useState } from "react";
import api from "../config/api";

//Creacion de un componente especifico
function AnioSeccionForm() {
    //Creacion del estado inicial de las areas del formulario
    const [formData, setFormData] = useState({
        anio: '',
        seccion: ''
    });

    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);
    const [success, setSuccess] = useState(false);

    //Declaracion de una funcion para manejar los cambios en los inputs
    const handleChange = (e) => {
        const {name, value} = e.target;
        if (value.length > 1) return;
        //Actualizar el estado manteniendo los otros campos intactos
        setFormData(prevState => ({
            ...prevState,
            [name]: value
        }));
        setError(null);
        setSuccess(false);
    };

    //Declaracion de una funcion para manejar el envio del formulario
    const handleSubmit = async (e) => {
        e.preventDefault();

        if (!formData.anio || !formData.seccion) {
            setError("Ambos campos son obligatorios");
            return;
        }

        setLoading(true);
        try{
            const response = await api.post('/anio-seccion/', formData);
            console.log("Creado:", response.data);
            setSuccess(true);
            setFormData({anio: '', seccion: ''});
        } catch (err){
            console.error(err);
            if (err.response?.data?.detail){
                setError(err.response.data.detail);
            } else {
                setError("Error de conexion con el servidor");
            }
        } finally {
            setLoading(false);
        }
    };

    return(
        <div className="form-container">
            <h2>Registrar Año y Sección</h2>
            {/* Asignacion de handleSubmit para cuando se envie el formulario */}
            <form onSubmit={handleSubmit}>
                <div className="form-group">
                    <label htmlFor="anio">Año (1 dígito):</label>
                    {/* Vinculacion de value y de la funcion onChange */}
                    <input 
                        type="text"
                        id="anio"
                        name="anio"
                        value={formData.anio}
                        onChange={handleChange}
                        placeholder="Ej.: 1"
                        maxLength={1}
                        disabled={loading}
                    />
                </div>
                <div className="form-group">
                    <label htmlFor="seccion">Sección (1 caracter):</label>
                    <input 
                        type="text" 
                        name="seccion" 
                        id="seccion"
                        value={formData.seccion}
                        onChange={handleChange}
                        placeholder="Ej.: A"
                        maxLength={1}
                        disabled={loading}
                    />
                </div>
                <button type="submit" disabled={loading}>
                    {loading ? 'Guardando...' : 'Guardar'}
                </button>
            </form>
        </div>
    );
}

export default AnioSeccionForm