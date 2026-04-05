import { useState, useEffect, useTransition } from "react";
import api from "../../config/api";

function EstudianteForm() {
    const [formData, setFormData] = useState({
        ci: '',
        primer_nom: '',
        segundo_nom: '',
        primer_ape: '',
        segundo_ape: '',
        anio_seccion_id: ''
    });

    const [anioSecciones, setAnioSecciones] = useState([]);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);
    const [success, setSuccess] = useState(false);

    //Cargar los años y secciones disponibles
    useEffect(() => {
        fetchAnioSecciones();
    }, []);

    const fetchAnioSecciones = async () => {
        try{
            const response = await api.get('/anio-seccion/');
            console.log(response.data)
            setAnioSecciones(response.data);
        } catch (err) {
            console.error('Error al cargar los años/secciones:', err);
        }
    };

    const handleChange = async (e) => {
        const {name, value} = e.target;
        setFormData(prev => ({...prev, [name]:value}));
        setError(null);
        setSuccess(false);
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (!formData.ci || !formData.primer_nom || !formData.primer_ape || !formData.segundo_ape) {
            setError('Por favor, rellene todos los campos obligatorios');
            return;
        }
        if (!formData.anio_seccion_id) {
            setError('Selecciona un año y seccion');
            return;
        }
        setLoading(true);
        try {
            //convertir ci y anio_seccion a numero o null
            const datosEnviar = {
                ...formData,
                ci: parseInt(formData.ci),
                anio_seccion_id: formData.anio_seccion_id ? parseInt(formData.anio_seccion_id): null
            };
            await api.post('/estudiante/', datosEnviar);
            setSuccess(true);
            setFormData({
                ci: '',
                primer_nom: '',
                segundo_nom: '',
                primer_ape: '',
                segundo_ape: '',
                anio_seccion_id: ''
            });
        } catch (err) {
            console.error('Error al crear el estudiante', err);
            const mensaje = err.response?.data?.detail || 'Error al registrar estudiante';
            setError(mensaje);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="form-container">
            <h2>Registrar Estudiante</h2>
            {success && (
                <div className="alert alert-success">
                    ✅ Estudiante registrado correctamente
                </div>
            )}

            {error && (
                <div className="alert alert-error">
                    ❌  {error}
                </div>
            )}

            <form onSubmit={handleSubmit}>
                <div className="form-row">
                    <div className="form-group">
                        <label htmlFor="ci">CI *</label>
                        <input 
                            type="number"
                            id="ci"
                            name="ci"
                            value={formData.ci}
                            onChange={handleChange}
                            placeholder="Ej: 12345678"
                            disabled={loading}
                            required
                        />
                    </div>

                    <div className="form-group">
                        <label htmlFor="anio_seccion_id">Año / Seccion</label>
                        <select 
                            name="anio_seccion_id" 
                            id="anio_seccion_id"
                            value={formData.anio_seccion_id}
                            onChange={handleChange}
                            disabled={loading}
                            required
                        >
                            <option value="">Seleccionar...</option>
                            {anioSecciones.map((as) => {
                                <option key={as.id} value={as.id}>
                                    {as.anio}° "{as.seccin}"
                                </option>
                            })}
                        </select>
                    </div>
                </div>

                <div className="form-row">
                    <div className="form-group">
                        <label htmlFor="primer_nom">Primer Nombre *</label>
                        <input 
                            type="text" 
                            id="primer_nom"
                            name="primer_nom"
                            value={formData.primer_nom}
                            onChange={handleChange}
                            placeholder="Ej: Pedro"
                            maxLength={50}
                            disabled={loading}
                            required
                        />
                    </div>

                    <div className="form-group">
                        <label htmlFor="segundo_nom">Segundo Nombre</label>
                        <input 
                            type="text" 
                            id="segundo_nom"
                            name="segundo_nom"
                            value={formData.segundo_nom}
                            onChange={handleChange}
                            placeholder="Ej: Jose"
                            maxLength={50}
                            disabled={loading}
                            required
                        />
                    </div>

                    <div className="form-group">
                        <label htmlFor="primer_ape">Primer Apellido *</label>
                        <input 
                            type="text" 
                            id="primer_ape"
                            name="primer_ape"
                            value={formData.primer_ape}
                            onChange={handleChange}
                            placeholder="Ej: Perez"
                            maxLength={50}
                            disabled={loading}
                            required
                        />
                    </div>

                    <div className="form-group">
                        <label htmlFor="segundo_ape">Segundo Apellido *</label>
                        <input 
                            type="text" 
                            id="segundo_ape"
                            name="segundo_ape"
                            value={formData.segundo_ape}
                            onChange={handleChange}
                            placeholder="Ej: Maldonado"
                            maxLength={50}
                            disabled={loading}
                            required
                        />
                    </div>
                </div>

                <button type="submit" disabled={loading} className="btn-submit">
                    {loading ? '⏳ Registrando...' : '💾 Registrar Estudiante'}
                </button>
            </form>
        </div>
    );
}

export default EstudianteForm;