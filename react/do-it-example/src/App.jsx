import { Component } from 'react';
import ChildComponent2 from './03/ChildComponent2';

class App extends Component {
  render() {
    return (
      <div>
        <ChildComponent2 objValue={{ age: 20 }} requiredStringValue="문자" />
      </div>
    );
  }
}

export default App;
