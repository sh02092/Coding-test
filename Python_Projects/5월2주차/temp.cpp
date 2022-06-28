using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Unity.MLAgents;
using Unity.MLAgents.Sensors;
using Unity.MLAgents.Actuators;

public class CarAgent : Agent
{
    private Transform tr;
    private Rigidbody rb;


    public float moveSpeed;
    public float Turn;
    Vector3 startPosition;
    Vector3 startRotation;

    public override void Initialize()
    {
        //MaxStep = 5000;
        tr = GetComponent<Transform>();
        rb = GetComponent<Rigidbody>();
        startPosition = tr.position;
        startRotation = tr.eulerAngles;
    }

    public override void OnEpisodeBegin()
    {
        // 물리엔진 초기화
        rb.velocity = Vector3.zero;
        rb.angularVelocity = Vector3.zero;

        // 위치 초기화
        tr.position = startPosition;
        tr.eulerAngles = startRotation;

    }

    public override void CollectObservations(VectorSensor sensor)
    {

    }

    public override void OnActionReceived(ActionBuffers actions)
    {
        int action = actions.DiscreteActions[0];

        if (action == 0) Turn = -0.5f; moveSpeed = 5.0f;
        if (action == 1) Turn = -0.5f; moveSpeed = 7.5f;
        if (action == 2) Turn = -0.5f; moveSpeed = 10.0f;
        if (action == 3) Turn = 0f; moveSpeed = 5.0f;
        if (action == 4) Turn = 0f; moveSpeed = 7.5f;
        if (action == 5) Turn = 0f; moveSpeed = 10.0f;
        if (action == 6) Turn = 0.5f; moveSpeed = 5.0f;
        if (action == 7) Turn = 0.5f; moveSpeed = 7.5f;
        if (action == 8) Turn = 0.5f; moveSpeed = 10.0f;
        if (action == 9) Turn = -1.3f; moveSpeed = 5.0f;
        if (action == 10) Turn = -1.3f; moveSpeed = 7.5f;
        if (action == 11) Turn = -1.3f; moveSpeed = 10.0f;
        if (action == 12) Turn = 1.3f; moveSpeed = 5.0f;
        if (action == 13) Turn = 1.3f; moveSpeed = 7.5f;
        if (action == 14) Turn = 1.3f; moveSpeed = 10.0f;

        transform.Translate(moveSpeed * Time.fixedDeltaTime * Vector3.forward);
        //transform.Rotate(0f, Turn, 0f);
        transform.Rotate(new Vector3(0f, Turn, 0f));
    }

    public override void Heuristic(in ActionBuffers actionsOut)
    {
        int actionOut = actionsOut.DiscreteActions[0];
        // 왼쪽
        if (Input.GetKey(KeyCode.LeftArrow)) actionOut = 9;

        // 직진
        if (Input.GetKey(KeyCode.UpArrow)) actionOut = 3;

        // 오른쪽
        if (Input.GetKey(KeyCode.RightArrow)) actionOut = 12;
    }


    void OnCollisionEnter(Collision collision)
    {
        if (collision.collider.CompareTag("wall") || collision.collider.CompareTag("neighbor"))
        {
            //AddReward(-1.0f);
            EndEpisode();
        }
    }
}



// Ray Perception Sensor 3D의 역할
// 거리에 따라서 Reward 값을 다르게 지정해주는지...?
// 