using System.Collections;
using System.Collections.Generic;
using UnityEngine;

[RequireComponent(typeof(CharacterController))]
public class Mover : MonoBehaviour
{
    //move
    public CharacterController Char;
    public Joystick joystick;
    public GameObject jumpbutton;
    public float speed = 10.0f;
    public float jumpspeed = 10.0f;
    public float gravity = 9.8f;
    public GameObject rotatearea;

    //rotate
    Touch touch;
    Vector2 touchPos;
    Quaternion rotY;
    public float rotate_speed = 0.1f;

    // Start is called before the first frame update
    void Start()
    {

        if (!Char)
        {

            Char = GetComponent<CharacterController>();

        }

    }

    // Update is called once per frame
    void Update()
    {
        //move
        Vector3 X = joystick.Horizontal * Vector3.right * Time.deltaTime * speed;
        Vector3 Z = joystick.Vertical * Vector3.forward * Time.deltaTime * speed;
        Vector3 Y = 0 * Vector3.up;
        if (Char.isGrounded && jumpbutton.GetComponent<jumpbuttoncode>().pressed)
        {

            Y = Vector3.up * Time.deltaTime * jumpspeed * 30;

        }
        Vector3 movement = transform.TransformDirection(X + Y + Z);
        movement.y -= gravity * Time.deltaTime;
        Char.Move(movement);

        //rotate
        if (rotatearea.GetComponent<oncilckrotate>().pressed && Input.touchCount > 0)
        {

            touch = Input.GetTouch(0);
            if(touch.phase == TouchPhase.Moved)
            {

                rotY = Quaternion.Euler(0.0f, -touch.deltaPosition.x * rotate_speed, 0.0f);

            }
            transform.rotation = rotY * transform.rotation;

        }
    }
}
