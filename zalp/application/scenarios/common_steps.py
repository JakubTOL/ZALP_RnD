from zalp.application.scenarios import Step, Scenario


class CameraInitializationStep(Step):
    name = 'Inicjalizacja kamery'
    description = """Kamera została zasilona i jest w trakcie inicjalizacji. Może to zajęć do 15 sekund.
    Status kamery można obserwować w zakładce "Rx" w polach "Status kamery"."""
    minimum_time = 5  # s

    # TODO: waitable or not?

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dtc_clear_requested = False

    def pre(self):
        self.app.video_player.load_default_driving_video()
        self.app.psu_service.set_output()

        # self.app.can_manager.reset_signals()
        # self.app.can_manager.set_default_values()  # Skipped - this should be done before the scenario is started
        # self.app.can_manager.send_vin_frame()

    def during(self):
        # Clear DTCs 5 s after power-up
        if not self.dtc_clear_requested and self.has_elapsed_time(self.minimum_time):
            self.app.can_manager.can1.clear_all_dtcs()
            self.dtc_clear_requested = True

    def is_done(self) -> bool:
        # Check signal only after 5 s
        return self.has_elapsed_time(self.minimum_time) and \
            self.app.can_manager.signal_mapping.camera_status.PP_Vision_Status.get() == 'Vision'

    def post(self):
        pass
        # self.app.can_manager.enable_aeb()


class Step1(Step):
    pass

class Step2(Step):
    pass

class Step3(Step):
    pass


class ExampleScenario(Scenario):
    name = 'Przykładwowa nazwa scenariusza'
    description = 'To jest przykładowy opis scenariusza.'
    steps = (
        CameraInitializationStep,
        Step1,
        Step2,
        Step3
    )


