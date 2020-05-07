import argparse
import datetime
import os
import time
import paho.mqtt.client as mqtt
import random

def parse_command_line_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description=(
            'Device Simulator.'))

    parser.add_argument(
            '--device_id', 
            required=True, 
            help='IoT device id')

    parser.add_argument(
            '--num_messages',
            type=int,
            default=10,
            help='Number of messages to publish.')

    parser.add_argument(
            '--message_type',
            #choices=('event', 'state'),
            default='temperature',
            #required=True,
            help=('Indicates whether the message to be published is a '
                  'telemetry event or a device state message.'))

    parser.add_argument(
            '--mqtt_server',
            default='192.168.15.22',
            help='MQTT Server address.')

    parser.add_argument(
            '--mqtt_server_port',
            default=1883,
            type=int,
            help='MQTT server port.')

    return parser.parse_args()

def createSimulatedData(): 
    simulated_data = 10 + random.random() * 20

    if random.random() > 0.5:
        data_trend = +1     
    else:
        data_trend = -1
    
    simulated_data = simulated_data + data_trend * random.normalvariate(0.01,0.005)
    return simulated_data

def main():
    args = parse_command_line_args()
    mqtt_topic = '/devicesTelemetry/{}/{}/'.format(args.device_id,args.message_type)
    print('Publishing messages in {}:'.format(args.mqtt_server))
    client = mqtt.Client()
    client.connect(args.mqtt_server, args.mqtt_server_port)
    client.loop_start()
    
    for i in range(1, args.num_messages + 1):
        payload = '{:.2f}'.format(createSimulatedData())
        print('message {}/{}-{}'.format(i, args.num_messages, mqtt_topic+payload))
        client.publish(mqtt_topic, payload, qos=1)
        time.sleep(1)

    client.loop_stop()
    print('Finished.')


if __name__ == '__main__':
    main()