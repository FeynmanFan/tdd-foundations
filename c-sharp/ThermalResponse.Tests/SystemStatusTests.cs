namespace ThermalResponse.Tests
{
    public class SystemStatusTests
    {
        [Fact]
        public void BelowMin_NeedsHeater()
        {
            var system = new SystemStatus();
            var temp = SystemStatus.MINIMUM_TEMPERATURE - 1; // ice, ice baby

            var result = system.CheckTemp(temp);

            Assert.Equal(TemperatureStatus.HeaterNeeded, result);
        }

        [Fact]
        public void AboveMin_Nominal()
        {
            var system = new SystemStatus();
            var temp = SystemStatus.MINIMUM_TEMPERATURE + 1; // 126C

            var result = system.CheckTemp(temp);

            Assert.Equal(TemperatureStatus.Nominal, result);
        }

        [Fact]
        public void AboveMax_NeedsCooling()
        {
            var system = new SystemStatus();
            var temp = SystemStatus.MAXIMUM_TEMPERATURE + 1; // super-hot

            var result = system.CheckTemp(temp);

            Assert.Equal(TemperatureStatus.CoolingNeeded, result);
        }

        [Fact]
        public void AtMax_Nominal()
        {
            // arrange
            var system = new SystemStatus();
            var temp = SystemStatus.MAXIMUM_TEMPERATURE;

            // act
            var result = system.CheckTemp(temp);

            // assert
            Assert.Equal(TemperatureStatus.Nominal, result);
        }


        [Fact]
        public void AtMin_Nominal()
        {
            // arrange
            var system = new SystemStatus();
            var temp = SystemStatus.MINIMUM_TEMPERATURE;

            // act
            var result = system.CheckTemp(temp);

            // assert
            Assert.Equal(TemperatureStatus.Nominal, result);
        }
    }
}
