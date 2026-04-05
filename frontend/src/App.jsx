//Importacion de los componentes especificos
import { useState } from "react";
import Navbar from "./components/Navbar";
import AnioSeccionForm from "./components/AnioSeccion/AnioSeccionForm"
import AnioSeccionTable from "./components/AnioSeccion/AnioSeccionTable"
import EstudianteForm from "./components/Estudiante/EstudianteForm";
import EstudianteTable from "./components/Estudiante/EstudianteTable";

function App() {
  const [seccionActiva, setSeccionActiva] = useState('anio-seccion');

  const renderSeccion = () => {
    switch (seccionActiva) {
      case 'anio-seccion':
        return (
          <div className="seccion-content">
            <AnioSeccionForm />
            <AnioSeccionTable />
          </div>
        );
      case 'estudiantes':
        return (
          <div className="seccion-content">
            <EstudianteForm />
            <EstudianteTable />
          </div>
        );
      case 'notas':
        return (
          <div className="seccion-content">
            <div className="coming-soon">
              <h2>En construcción</h2>
              <p>Esta seccion de notas estara disponible proximamente</p>
            </div>
          </div>
        );
      default: 
        return null;
    }
  };

  return (
    <div className="App">
      <Navbar seccionActiva={seccionActiva} cambiarSeccion={setSeccionActiva} />
      <main className="app-main">
        {renderSeccion()}
      </main>
    </div>
  );
}

export default App