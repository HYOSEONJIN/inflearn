import React from "react";

class ForceUpdateExample extends React.Component {
  constructor(props) {
    super(props);
    //state 정의
    this.loading = true;
    this.formData = "no data";

    //이후 콜백 함수를 다룰 때 bind를 선언하는 부분에 대해 다룹니다
    this.handleData = this.handleData.bind(this);
    // 4초후 호출
    setTimeout(this.handleData, 4000);
  }
  handleData() {
    const data = "new data, ";
    //state 변경
    this.loading = false;
    this.formData = data + this.formData;
    // 컴포넌트 내장 함수 forceUpdate()를 호출하여 강제로 화면을 새로고침 한다.
    this.forceUpdate;
  }
  render() {
    return (
      <div>
        {/* 상태 데이터는 this.state로 접근 가능합니다. */}
        <span>로딩중: {String(this.state.loading)}</span>
        <span>결과: {this.state.formData}</span>
      </div>
    );
  }
}

export default ForceUpdateExample;
C;
