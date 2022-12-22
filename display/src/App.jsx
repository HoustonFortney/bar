import menu from './data/menu.json';

function Drink(props) {
  const { drink } = props;

  const componentsList = drink.components.map((component) => component.replaceAll(' ', '\xa0')).join(', ');

  return (
    <div className="my-2">
      <h3 className="fs-5 mb-0">{drink.name}</h3>
      <p className="m-0">{componentsList}</p>
    </div>
  );
}

function Section(props) {
  const { section } = props;

  return (
    <div className="my-5">
      <h2 className="mb-4">{section.name}</h2>
      {section.drinks.map((drink) => <Drink key={drink.name} drink={drink} />)}
    </div>
  );
}

function App() {
  return (
    <div className="d-flex align-items-center justify-content-center">
      <div className="m-3 p-3 section" style={{ maxWidth: 450 }}>
        {menu.sections.map((section) => <Section key={section.name} section={section} />)}
      </div>
    </div>
  );
}

export default App;
