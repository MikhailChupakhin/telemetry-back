import time
import random


def generate_random_float(min_val, max_val, precision=2):
    precision = max(0, min(6, precision))
    random_value = random.uniform(min_val, max_val)
    rounded_value = round(random_value, precision)
    return rounded_value


def generate_random_runtime_data():
    return {
        "timestamp": int(time.time()),
        "sensors": {
            "pitot": {"timestamp": 0, "pressure": 0.0, "speed": 0.0, "speed_filtered": 0.0},
            "distance": {
                "left": {"timestamp": 0, "raw": 0, "cleaned": 0, "filtered": 0},
                "right": {"timestamp": 0, "raw": 0, "cleaned": 0, "filtered": 0},
                "front_filtered": generate_random_float(0, 10, 0),
                "sweep": 1,
                "angle": -0.0,
                "diff": 0,
            },
            "imu": {
                "timestamp": 678333,
                "orientation": {
                    "roll": generate_random_float(-1, 1, 5),
                    "pitch": generate_random_float(-1, 1, 5),
                    "heading": 0.03845,
                },
                "angular": [0.06104, 0.12207, -0.0],
                "acceleration": [-0.00879, -0.01562, 1.00391],
                "magnetic": [27731, 30635, 32545],
                "pressure": 97001.0,
                "temperature": 30.49,
            },
            "gps": {
                "timestamp": 1788,
                "speed": 2.0,
                "speed_knots": 0.0,
                "satellites": 0,
                "date": "00.00.2000",
                "time": "00:00:00.00",
            },
        },
        "angles": {"flaperon_left": 0.96988, "flaperon_right": -0.96988},
        "servo": {
            "flaperon_left": {
                "pos": -2077,
                "speed": 0,
                "rawpos": 0,
                "rawspeed": 0,
                "home": 0,
                "angle": -1.65083,
                "voltage": 0,
                "current": 0,
                "online": False,
            },
            "flaperon_right": {
                "pos": 1837,
                "speed": 0,
                "rawpos": 0,
                "rawspeed": 0,
                "home": 0,
                "angle": -5.51609,
                "voltage": 0,
                "current": 0,
                "online": False,
            },
        },
        "throttle_handle": {"timestamp": 0, "status": 0, "angle": 0, "power": 0},
        "motor": {
            "timestamp": 0,
            "rpm": 0,
            "voltage_in": 0.0,
            "current": 0.0,
            "motor_temperature": 0,
            "controller_temperature": 0,
            "throttle_percent": 0.0,
            "throttle_percent_cmd": 0.0,
        },
        "ui": {"speedometer": 0.0, "temperature": 30.49, "compas": 0.0},
        "state": "Locked",
        "speed_unreliable": True,
        "angle_front": 0.0,
        "angle_flaperon": 0.0,
        "angle_diff": 0.96988,
        "target_roll": 1.0,
        "target_pitch": 0.0,
        "target_level": 500,
        "stabilizer_lift": {
            "timestamp": 0,
            "status": {"magnet": {"strength": 0, "angle": 0}, "state": 0, "pos": 0},
        },
    }


example_parameters_data = {
    "timestamp": 725990,
    "sensors": {
        "pitot": {
            "kalman": {"measure": 2.0, "estimate": 2.0, "q": 2.0},
            "pressure_shift": 7000,
            "k": 1.15,
        },
        "distance": {
            "distance_kalman": {"measure": 120.0, "estimate": 5000.0, "q": 1.0},
            "slope": 400.0,
            "front_average_kalman": {"measure": 10.0, "estimate": 84000.0, "q": 0.01},
            "left": {"base": 1170},
            "right": {"base": 1170},
        },
        "steering": {
            "angular_kalman": {"measure": 3.0, "estimate": 3.0, "q": 0.1},
            "acceleration_kalman": {"measure": 3.0, "estimate": 3.0, "q": 0.1},
        },
        "imu": {"roll_shift": 0.0, "pitch_shift": 0.0},
    },
    "control_surfaces": {
        "flaperon_left": {
            "direct": False,
            "arm": 50.0,
            "leash": 55.0,
            "offset": -40.0,
            "lo": -10.0,
            "hi": 30.0,
            "neutral": 0.0,
            "test_angle": 0.0,
        },
        "flaperon_right": {
            "direct": False,
            "arm": 50.0,
            "leash": 55.0,
            "offset": -40.0,
            "lo": -10.0,
            "hi": 20.0,
            "neutral": 0.0,
            "test_angle": 0.0,
        },
        "flaperon_hi": 5.0,
        "flaperon_lo": -3.0,
    },
    "servos": {
        "flaperon_left": {
            "arm": 40.0,
            "offset": -2.0,
            "zero": -2200,
            "inv": True,
            "enabled": True,
            "voltage_on": True,
            "test_angle": 0.0,
        },
        "flaperon_right": {
            "arm": 40.0,
            "offset": -3.0,
            "zero": 2250,
            "inv": False,
            "enabled": True,
            "voltage_on": True,
            "test_angle": 0.0,
        },
        "flaperon_speed": 90.0,
        "drive": {
            "limits": {
                "torque": 1000,
                "acceleration": 10000,
                "speed": 1000,
                "travel": 70.0,
            },
            "encoder_resolution": 1000,
            "gearbox": {"mult": 1, "div": 27},
            "regulator": {"P": 0.25, "I": 0.2, "D": 25.0, "MC": 4.0},
        },
        "homing": {
            "limits": {
                "torque": 200,
                "acceleration": 10000,
                "speed": 2000,
                "travel": 100.0,
            },
            "precision": 20.0,
            "timeout": 300,
            "up": False,
        },
    },
    "regulators": {
        "level": {"P": 20.0, "I": 1.0, "D": 40.0, "MC": 1.0},
        "roll": {"P": 10.0, "I": 1.0, "D": 40.0, "MC": 1.0},
        "pitch": {"P": 300.0, "I": 9.0, "D": 40.0, "MC": 1.0},
    },
    "speed_thresholds": {
        "crawling": {"lo": 0.1, "hi": 0.2},
        "cruising": {"lo": 3.0, "hi": 4.0},
    },
    "takeoff_speed": 4.0,
    "landing_speed": 4.0,
    "levels": {"lo": 200, "hi": 500},
    "wave_length": 5.0,
    "max_roll_angle": 3.0,
    "critical_roll_angle": 5.0,
    "max_pitch_angle": 3.0,
    "throttle": {
        "limits": {"lo": -12700, "hi": 13300},
        "dead_zone": {"lo": -1300, "hi": 500},
    },
    "crawling_pitch": 5.0,
    "acceleration_level": {"lo": 820, "hi": 820},
    "geometry": {
        "rotation_center": {"y": 1515.0, "z": 0.0},
        "front_wing": {"y": 0.0, "z": 0.0},
        "aft_wing": {"y": 0.0, "z": 0.0},
    },
    "turn_roll": False,
    "motor": {"can_mode": 1, "gear": 2},
    "stabilizer_lift": {
        "drive": {
            "limits": {
                "torque": 1000,
                "acceleration": 10000,
                "speed": 1000,
                "travel": 70.0,
            },
            "encoder_resolution": 1000,
            "gearbox": {"mult": 1, "div": 27},
            "regulator": {"P": 0.25, "I": 0.2, "D": 25.0, "MC": 4.0},
        },
        "homing_limits": {
            "torque": 200,
            "acceleration": 10000,
            "speed": 2000,
            "travel": 100.0,
        },
        "inv": False,
        "screw_step": 3.0,
        "magnet": {
            "polarity": False,
            "level_detected": 1,
            "level_up": 10,
            "level_dn": 10,
        },
    },
    "controls": {"lift_up": False, "lift_dn": False, "key": False, "archimedes": False},
}
