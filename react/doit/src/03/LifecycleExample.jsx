import React from "react";

class LifecycleExample extends React.Component {
  static getDerivedStateFromProps() {
    console.log("getDerivedStateFromProps 호출");
    return {};
  }

  constructor(props) {
    super(props);
    //getDerivedStateFromProps()함수를 사용하므로
    //경고메세지를 건너뛰기 위해 state 초기값 설정

    this.state = {};
    console.log("constructor 호출");
  }

  componentDidMount() {
    console.log("ComponentDidMount 호출");
  }

  componentDidUpdate() {
    console.log("ComponentDidUpdate 호출");
  }

  componentWillUnmount() {
    console.log("ComponentWillUnmount 호출");
    return {};
  }

  getSnapshotBeforeUpdate() {
    console.log("getSnapshotBeforeUpdate 호출");
    return {};
  }

  shouldComponentUpdate() {
    console.log("shouldComponentUpdate 호출");
    return true;
  }

  render() {
    console.log("render 호출");
    return null;
  }
}

export default LifecycleExample;
