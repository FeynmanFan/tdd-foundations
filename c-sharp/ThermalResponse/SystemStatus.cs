namespace ThermalResponse
{
    public class SystemStatus
    {
        // TODO: Implement checks for this when we have time
        public const decimal MINIMUM_TEMPERATURE = 160.15m; // Kelvin, -113C
        public const decimal MAXIMUM_TEMPERATURE = 723.15m; // Kelvin, 450C

        public SystemStatus()
        {

        }

        public TemperatureStatus CheckTemp(decimal temp)
        {
            if (temp < MINIMUM_TEMPERATURE)
            {
                return TemperatureStatus.HeaterNeeded;
            }

            if (temp <= MAXIMUM_TEMPERATURE)
            {
                return TemperatureStatus.Nominal;
            }

            return TemperatureStatus.CoolingNeeded;
        }
    }

    public enum TemperatureStatus
    {
        HeaterNeeded = 0,
        Nominal = 1,
        CoolingNeeded = 2
    }
}
