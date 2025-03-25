namespace ThermalResponse.Tests
{
    public class SystemStatusTests
    {
        [Fact]
        public void BelowMin_NeedsHeater()
        {
            var system = new SystemStatus();
            var temp = 150m; // ice, ice baby

            var result = system.CheckTemp(temp);

            Assert.Equal(TemperatureStatus.HeaterNeeded, result);
        }

        [Fact]
        public void AboveMin_Nominal()
        {
            var system = new SystemStatus();
            var temp = 400m; // 126C

            var result = system.CheckTemp(temp);

            Assert.Equal(TemperatureStatus.Nominal, result);
        }

        [Fact]
        public void AboveMax_NeedsCooling()
        {
            var system = new SystemStatus();
            var temp = 730m; // super-hot

            var result = system.CheckTemp(temp);

            Assert.Equal(TemperatureStatus.CoolingNeeded, result);
        }
    }
}
