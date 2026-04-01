//Importar el hook useState para poder controlar cambios en el form
import { useState } from "react";

//Creacion de un componente especifico
function ContactForm() {
    //Creacion del estado inicial de las areas del formulario
    const [formData, setFormData] = useState({
        nombre: '',
        email: '',
        mensaje: ''
    });

    //Declaracion de una funcion para manejar los cambios en los inputs
    const handleChange = (e) => {
        const {name, value} = e.target;
        //Actualizar el estado manteniendo los otros campos intactos
        setFormData(prevState => ({
            ...prevState,
            [name]: value
        }));
    };

    //Declaracion de una funcion para manejar el envio del formulario
    const handleSubmit = (e) => {
        e.preventDefault();

        //Validacion basica para evitar enviar campos vacios
        if (!formData.nombre || !formData.email || !formData.mensaje){
            alert("Por favor, rellene todos los campos");
            return;
        }

        //Validacion basica de email utilizando regex
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
        if (!emailRegex.test(formData.email)){
            alert("Por favor, introduzca un email valido");
            return;
        }

        //Aqui se hacen las operaciones con las API o el envio de datos
        console.log("Formulario enviado con los datos:", formData);
        alert("Mensaje envaido de forma exitosa");

        //Limpiar los datos del formulario despues del envio
        setFormData({
            nombre: '',
            email: '',
            mensaje: ''
        });
    };

    return(
        <div className="form-container">
            <h2>Contáctanos</h2>
            {/* Asignacion de handleSubmit para cuando se envie el formulario */}
            <form onSubmit={handleSubmit}>
                <div className="form-group">
                    <label htmlFor="nombre">Nombre:</label>
                    {/* Vinculacion de value y de la funcion onChange */}
                    <input 
                        type="text"
                        id="nombre"
                        name="nombre"
                        value={formData.nombre}
                        onChange={handleChange}
                    />
                </div>
                <div className="form-group">
                    <label htmlFor="email">Email:</label>
                    <input 
                        type="email" 
                        name="email" 
                        id="email"
                        value={formData.email}
                        onChange={handleChange}
                    />
                </div>
                <div className="form-group">
                    <label htmlFor="mensaje">Mensaje:</label>
                    <textarea 
                        name="mensaje" 
                        id="mensaje" 
                        rows="4"
                        value={formData.mensaje}
                        onChange={handleChange}
                    ></textarea>
                </div>
                <button type="submit">Enviar Mensaje</button>
            </form>
            {/* Para poder ver datos en tiempo real, opcional */}
            <pre>{JSON.stringify(formData, null, 2)}</pre>
        </div>
    );
}

export default ContactForm